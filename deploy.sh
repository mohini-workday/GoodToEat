#!/bin/bash

# Deployment script for GoodToEat Streamlit app
# Usage: ./deploy.sh

set -e

echo "🚀 Starting deployment for goodtoeatfoods.com..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if docker-compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ docker-compose is not installed. Please install docker-compose first."
    exit 1
fi

# Pull latest code (if using git)
if [ -d ".git" ]; then
    echo "📥 Pulling latest code..."
    git pull origin main
fi

# Build and start containers
echo "🔨 Building and starting containers..."
docker-compose down
docker-compose build --no-cache
docker-compose up -d

# Wait for services to be healthy
echo "⏳ Waiting for services to start..."
sleep 10

# Check if services are running
if docker ps | grep -q "goodtoeat-streamlit"; then
    echo "✅ Streamlit app is running!"
else
    echo "❌ Streamlit app failed to start. Check logs with: docker-compose logs streamlit-app"
    exit 1
fi

if docker ps | grep -q "goodtoeat-nginx"; then
    echo "✅ Nginx is running!"
else
    echo "❌ Nginx failed to start. Check logs with: docker-compose logs nginx"
    exit 1
fi

echo ""
echo "🎉 Deployment complete!"
echo "📊 Check status with: docker-compose ps"
echo "📝 View logs with: docker-compose logs -f"
echo "🌐 Your app should be available at: https://goodtoeatfoods.com"

