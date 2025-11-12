#!/bin/bash

# Student Result Analysis - Docker Setup Script

echo "🐳 Student Result Analysis - Docker Setup"
echo "=========================================="

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

echo "✅ Docker and Docker Compose are installed"
echo ""

# Menu
echo "Choose an option:"
echo "1. Build and start application"
echo "2. Stop application"
echo "3. View logs"
echo "4. Restart application"
echo "5. Remove containers and volumes"
echo "6. Build image only"

read -p "Enter your choice (1-6): " choice

case $choice in
    1)
        echo "🚀 Building and starting application..."
        docker-compose up --build
        ;;
    2)
        echo "⛔ Stopping application..."
        docker-compose down
        echo "✅ Application stopped"
        ;;
    3)
        echo "📋 Showing logs..."
        docker-compose logs -f student-analysis
        ;;
    4)
        echo "🔄 Restarting application..."
        docker-compose restart
        echo "✅ Application restarted"
        ;;
    5)
        echo "🗑️  Removing containers and volumes..."
        docker-compose down -v
        echo "✅ Cleanup complete"
        ;;
    6)
        echo "🔨 Building image..."
        docker-compose build
        echo "✅ Image built successfully"
        ;;
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac
