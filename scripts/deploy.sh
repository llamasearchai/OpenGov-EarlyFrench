#!/bin/bash
# Deployment script for OpenGov-EarlyFrench
# Author: Nik Jois <nikjois@llamasearch.ai>

set -e

echo "Deploying OpenGov-EarlyFrench..."

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if .env file exists
if [ ! -f .env ]; then
    echo -e "${RED}Error: .env file not found${NC}"
    echo -e "${YELLOW}Please create .env file from .env.example${NC}"
    exit 1
fi

# Build Docker images
echo -e "${YELLOW}Building Docker images...${NC}"
docker-compose build
echo -e "${GREEN}Docker images built${NC}"

# Stop existing containers
echo -e "${YELLOW}Stopping existing containers...${NC}"
docker-compose down
echo -e "${GREEN}Containers stopped${NC}"

# Start containers
echo -e "${YELLOW}Starting containers...${NC}"
docker-compose up -d
echo -e "${GREEN}Containers started${NC}"

# Wait for health check
echo -e "${YELLOW}Waiting for health check...${NC}"
sleep 10

# Check health
if curl -f http://localhost:8000/health > /dev/null 2>&1; then
    echo -e "${GREEN}Health check passed${NC}"
    echo -e "${GREEN}Deployment completed successfully!${NC}"
    echo -e "${GREEN}API available at: http://localhost:8000${NC}"
    echo -e "${GREEN}API docs available at: http://localhost:8000/docs${NC}"
else
    echo -e "${RED}Health check failed${NC}"
    echo -e "${YELLOW}Checking logs...${NC}"
    docker-compose logs api
    exit 1
fi

