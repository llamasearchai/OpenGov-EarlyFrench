from opengov_earlyfrench.core.verb_conjugator import VerbConjugator


def test_passe_compose_auxiliary_form_selection_branches() -> None:
    vc = VerbConjugator()

    # je + avoir path should use j'
    res_je = vc.form_passe_compose("parler", "je")
    assert res_je["auxiliary"] == "avoir"
    assert res_je["auxiliary_form"] in {"ai", "avais", "aurai", "aie"}
    assert res_je["complete_form"].startswith(" ") is False

    # subject substring match (il in "il/elle/on")
    res_il = vc.form_passe_compose("parler", "il")
    assert res_il["auxiliary_form"]  # picked from il/elle/on key

    # être auxiliary plus feminine agreement
    res_elle = vc.form_passe_compose("aller", "elle")
    assert res_elle["auxiliary"] == "être"
    assert res_elle["past_participle"].endswith("e")

    # feminine plural agreement
    res_elles = vc.form_passe_compose("aller", "elles")
    assert res_elles["past_participle"].endswith("es")


def test_regular_je_elision_and_second_group_and_past_participle() -> None:
    vc = VerbConjugator()
    # je elision to j'
    forms = vc.conjugate("aimer").get("forms", {})
    assert isinstance(forms, dict)
    assert "j'" in forms

    # second group detection
    from opengov_earlyfrench.core.models import VerbGroup

    group = vc._determine_verb_group("finir")  # type: ignore[attr-defined]
    assert group.value == VerbGroup.SECOND.value

    # third group past participle ends with 'u'
    pc = vc.form_passe_compose("vendre", "il")
    assert pc["past_participle"].endswith("u")

    # reflexive path basic coverage
    ref = vc.reflexive_verb("se lever")
    conj = ref.get("conjugation", {})
    assert isinstance(conj, dict)
    assert any(k.startswith("je ") or k.startswith("j'") for k in conj)

    # second group past participle 'i'
    pc2 = vc.form_passe_compose("finir", "il")
    assert pc2["past_participle"].endswith("i")
