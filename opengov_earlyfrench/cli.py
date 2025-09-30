"""CLI for OpenGov-EarlyFrench."""

from typing import Optional

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from opengov_earlyfrench import __version__
from opengov_earlyfrench.ai.conversation import AIConversationPartner
from opengov_earlyfrench.core.gender_teacher import GenderTeacher
from opengov_earlyfrench.core.pronunciation_coach import PronunciationCoach
from opengov_earlyfrench.core.verb_conjugator import VerbConjugator

app = typer.Typer(
    name="francais",
    help="OpenGov-EarlyFrench - AI-powered French language learning platform",
    add_completion=False,
)
console = Console()


@app.command()
def version() -> None:
    """Show version information."""
    console.print(f"[bold blue]OpenGov-EarlyFrench[/bold blue] version {__version__}")
    console.print("AI-powered French language learning platform")
    console.print("Author: Nik Jois <nikjois@llamasearch.ai>")


@app.command()
def pronunciation(
    text: Optional[str] = typer.Option(None, "--text", "-t", help="Text to analyze"),
    nasal: bool = typer.Option(False, "--nasal", "-n", help="Learn nasal vowels"),
    liaison: Optional[str] = typer.Option(None, "--liaison", "-l", help="Practice liaison"),
) -> None:
    """French pronunciation coaching and practice."""
    coach = PronunciationCoach()

    if nasal:
        lesson = coach.teach_nasal_vowels()
        console.print(Panel("[bold green]Nasal Vowels Lesson[/bold green]"))
        console.print(f"\n{lesson['explanation']}\n")

        for vowel_name, vowel_data in lesson["vowels"].items():
            console.print(f"[bold cyan]{vowel_name.upper()}[/bold cyan] {vowel_data['ipa']}")
            examples = vowel_data.get("examples", {})
            if isinstance(examples, dict):
                for french, english in list(examples.items())[:3]:
                    console.print(f"  • {french} - {english}")
            console.print()

        return

    if liaison:
        result = coach.practice_liaison(liaison)
        console.print(Panel(f"[bold green]Liaison Practice: {liaison}[/bold green]"))

        if "pronunciation" in result:
            console.print(f"[cyan]Pronunciation:[/cyan] {result['pronunciation']}")
            console.print(f"[cyan]Rule:[/cyan] {result['rule']}")
            console.print(f"[cyan]Type:[/cyan] {result['type']}")
        else:
            console.print(f"[yellow]{result.get('tip', 'No example found')}[/yellow]")

        return

    if text:
        analysis = coach.analyze_pronunciation(text)
        console.print(Panel("[bold green]Pronunciation Analysis[/bold green]"))
        console.print(f"[cyan]Text:[/cyan] {analysis.text}")
        console.print(f"[cyan]Score:[/cyan] {analysis.score:.1f}/100")

        if analysis.challenges:
            console.print("\n[yellow]Challenges:[/yellow]")
            for challenge in analysis.challenges:
                console.print(f"  • {challenge}")

        if analysis.improvements:
            console.print("\n[green]Improvements:[/green]")
            for improvement in analysis.improvements:
                console.print(f"  • {improvement}")

        return

    console.print(
        "[yellow]Use --text, --nasal, or --liaison flag. See --help for more info.[/yellow]"
    )


@app.command()
def conjugate(
    verb: str = typer.Argument(..., help="Verb to conjugate"),
    tense: str = typer.Option("présent", "--tense", "-t", help="Tense to conjugate"),
    reflexive: bool = typer.Option(False, "--reflexive", "-r", help="Reflexive verb"),
    subjunctive: bool = typer.Option(False, "--subjunctive", "-s", help="Subjunctive practice"),
) -> None:
    """Conjugate French verbs."""
    conjugator = VerbConjugator()

    if reflexive:
        result = conjugator.reflexive_verb(verb)
        console.print(Panel(f"[bold green]Reflexive Verb: {result['infinitive']}[/bold green]"))

        table = Table(show_header=True, header_style="bold cyan")
        table.add_column("Subject + Pronoun")
        table.add_column("Form")

        conjugation = result.get("conjugation", {})
        if isinstance(conjugation, dict):
            for subject, form in conjugation.items():
                table.add_row(subject, form)

        console.print(table)
        console.print(f"\n[yellow]Note:[/yellow] {result['note']}")
        return

    if subjunctive:
        result = conjugator.subjunctive_practice(verb)
        console.print(Panel(f"[bold green]Subjunctive Practice: {verb}[/bold green]"))

        forms = result.get("forms", {})
        if isinstance(forms, dict):
            table = Table(show_header=True, header_style="bold cyan")
            table.add_column("Subject")
            table.add_column("Form")

            for subject, form in forms.items():
                table.add_row(subject, form)

            console.print(table)

        console.print("\n[cyan]Trigger Phrases:[/cyan]")
        triggers = result.get("trigger_phrases", [])
        if isinstance(triggers, list):
            for trigger in triggers[:5]:
                console.print(f"  • {trigger}")

        return

    from opengov_earlyfrench.core.models import Tense

    tense_map = {
        "présent": Tense.PRESENT,
        "imparfait": Tense.IMPARFAIT,
        "futur_simple": Tense.FUTUR_SIMPLE,
        "passé_composé": Tense.PASSE_COMPOSE,
    }

    selected_tense = tense_map.get(tense, Tense.PRESENT)
    result = conjugator.conjugate(verb, selected_tense)

    console.print(Panel(f"[bold green]Conjugation: {verb}[/bold green]"))
    console.print(f"[cyan]Tense:[/cyan] {result.get('tense', tense)}")

    forms = result.get("forms", {})
    if isinstance(forms, dict):
        table = Table(show_header=True, header_style="bold cyan")
        table.add_column("Subject")
        table.add_column("Form")

        for subject, form in forms.items():
            table.add_row(subject, form)

        console.print(table)

        if result.get("type") == "irregular":
            console.print("\n[yellow]Type:[/yellow] Irregular verb")
            console.print(f"[yellow]Auxiliary:[/yellow] {result.get('auxiliary')}")
            console.print(f"[yellow]Past Participle:[/yellow] {result.get('past_participle')}")
    else:  # pragma: no cover - defensive path
        console.print(f"[red]Error:[/red] {result.get('error', 'Unknown error')}")


@app.command()
def gender(
    word: str = typer.Argument(..., help="Word to analyze"),
    partitive: bool = typer.Option(False, "--partitive", "-p", help="Practice partitive articles"),
    contractions: bool = typer.Option(False, "--contractions", "-c", help="Learn contractions"),
) -> None:
    """Learn French noun gender patterns."""
    teacher = GenderTeacher()

    if partitive:
        result = teacher.partitive_practice()
        console.print(Panel("[bold green]Partitive Articles Practice[/bold green]"))
        console.print(f"\n{result['explanation']}\n")

        examples = result.get("examples", {})
        if isinstance(examples, dict):
            table = Table(show_header=True, header_style="bold cyan")
            table.add_column("French")
            table.add_column("English")

            for french, english in examples.items():
                table.add_row(french, english)

            console.print(table)

        console.print("\n[cyan]Rules:[/cyan]")
        rules = result.get("rules", [])
        if isinstance(rules, list):
            for rule in rules:
                console.print(f"  • {rule}")

        return

    if contractions:
        result = teacher.get_contractions()
        console.print(Panel("[bold green]Article Contractions[/bold green]"))

        rules = result.get("rules", {})
        if isinstance(rules, dict):
            table = Table(show_header=True, header_style="bold cyan")
            table.add_column("Original")
            table.add_column("Contraction")

            for original, contraction in rules.items():
                table.add_row(original, contraction)

            console.print(table)

        console.print(f"\n[yellow]Tip:[/yellow] {result.get('tip', '')}")
        return

    result = teacher.identify_pattern(word)
    console.print(Panel(f"[bold green]Gender Analysis: {word}[/bold green]"))

    likely_gender = result.get("likely_gender", "unknown")
    if likely_gender == "masculine":
        console.print("[blue]Gender:[/blue] [bold]Masculine[/bold] (le/un)")
    elif likely_gender == "feminine":
        console.print("[magenta]Gender:[/magenta] [bold]Feminine[/bold] (la/une)")
    else:
        console.print("[yellow]Gender:[/yellow] Unknown - memorization needed")

    console.print(f"\n[cyan]Rule:[/cyan] {result.get('rule', 'No pattern')}")

    if result.get("reliability"):
        console.print(f"[cyan]Reliability:[/cyan] {result['reliability']}")

    if result.get("is_exception"):
        console.print("\n[red]Warning:[/red] This word is an exception to the rule!")


@app.command()
def chat(
    level: str = typer.Option("A1", "--level", "-l", help="CEFR level (A1, A2, B1, B2, C1, C2)"),
) -> None:
    """Chat with AI French conversation partner."""
    console.print(Panel("[bold green]French Conversation Partner[/bold green]"))
    console.print(f"Level: {level}")
    console.print("Type 'exit' or 'quit' to end conversation.\n")

    partner = AIConversationPartner(level=level)

    while True:
        try:
            user_input = typer.prompt("\n[You]", prompt_suffix=" ")

            if user_input.lower() in ["exit", "quit", "q"]:
                console.print("\n[yellow]Au revoir![/yellow]")
                break

            response = partner.chat(user_input)

            console.print(f"\n[bold blue][AI][/bold blue] {response.french}")
            console.print(f"[dim]{response.english}[/dim]")

            if response.grammar_notes:
                console.print(f"\n[cyan]Grammar:[/cyan] {', '.join(response.grammar_notes)}")

            if response.vocabulary:
                console.print(f"[cyan]Vocabulary:[/cyan] {', '.join(response.vocabulary[:3])}")

            if response.cultural_tips:
                console.print(f"[green]Cultural Tip:[/green] {response.cultural_tips[0]}")

        except KeyboardInterrupt:  # pragma: no cover - interactive
            console.print("\n\n[yellow]Au revoir![/yellow]")
            break
        except Exception as e:  # pragma: no cover - interactive
            console.print(f"\n[red]Error:[/red] {e}")


@app.command()
def scenario(
    scenario_type: str = typer.Argument("café", help="Scenario type (café, marché)"),
) -> None:
    """Practice with conversation scenarios."""
    partner = AIConversationPartner()
    result = partner.scenario(scenario_type)

    console.print(Panel(f"[bold green]Scenario: {result['setting']}[/bold green]"))
    console.print(f"\n[bold]{result['dialogue']}[/bold]")
    console.print(f"[dim]{result['english']}[/dim]\n")

    console.print("[cyan]Vocabulary:[/cyan]")
    vocabulary = result.get("vocabulary", {})
    if isinstance(vocabulary, dict):
        for french, english in list(vocabulary.items())[:5]:
            console.print(f"  • {french} - {english}")

    console.print("\n[cyan]Useful Phrases:[/cyan]")
    phrases = result.get("useful_phrases", [])
    if isinstance(phrases, list):
        for phrase in phrases:
            console.print(f"  • {phrase}")

    if result.get("cultural_tips"):
        console.print("\n[green]Cultural Tips:[/green]")
        tips = result["cultural_tips"]
        if isinstance(tips, list):
            for tip in tips:
                console.print(f"  • {tip}")


@app.command()
def serve(
    host: str = typer.Option("0.0.0.0", "--host", "-h", help="Host to bind to"),
    port: int = typer.Option(8000, "--port", "-p", help="Port to bind to"),
    reload: bool = typer.Option(False, "--reload", "-r", help="Enable auto-reload"),
) -> None:
    """Start the FastAPI server."""
    import uvicorn

    console.print(f"[green]Starting server on {host}:{port}...[/green]")
    console.print(f"[cyan]API docs available at http://{host}:{port}/docs[/cyan]")

    uvicorn.run(
        "opengov_earlyfrench.api.main:app",
        host=host,
        port=port,
        reload=reload,
    )


if __name__ == "__main__":  # pragma: no cover
    app()
