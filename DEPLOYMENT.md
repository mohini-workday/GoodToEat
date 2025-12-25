# Deployment Guide for goodtoeatfoods.com

This guide will help you deploy the GoodToEat Streamlit application to your custom domain `goodtoeatfoods.com`.

## Prerequisites

1. **Domain Access**: You need access to your domain's DNS settings
2. **Server/VPS**: A server with:
   - Ubuntu 20.04+ or similar Linux distribution
   - Docker and Docker Compose installed
   - At least 2GB RAM and 10GB storage
   - Root or sudo access

## Option 1: Deploy to VPS/Server (Recommended)

### Step 1: Set Up Your Server

1. **Connect to your server via SSH:**
   ```bash
   ssh user@your-server-ip
   ```

2. **Install Docker and Docker Compose:**
   ```bash
   # Update system
   sudo apt update && sudo apt upgrade -y

   # Install Docker
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER

   # Install Docker Compose
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose

   # Log out and back in for group changes to take effect
   ```

### Step 2: Clone Your Repository

```bash
cd /opt
sudo git clone https://github.com/mohini-workday/GoodToEat.git
cd GoodToEat
sudo chown -R $USER:$USER .
```

### Step 3: Set Up SSL Certificates

Install Certbot for Let's Encrypt SSL certificates:

```bash
sudo apt install certbot python3-certbot-nginx -y
```

### Step 4: Configure DNS

Add these DNS records in your domain provider's control panel:

**A Record:**
- Name: `@` (or `goodtoeatfoods.com`)
- Value: Your server's IP address
- TTL: 3600

**A Record (for www):**
- Name: `www`
- Value: Your server's IP address
- TTL: 3600

Wait 5-10 minutes for DNS propagation.

### Step 5: Obtain SSL Certificate

```bash
# Stop nginx temporarily
sudo docker-compose down

# Get SSL certificate
sudo certbot certonly --standalone -d goodtoeatfoods.com -d www.goodtoeatfoods.com

# Copy certificates to project directory
sudo mkdir -p ssl
sudo cp /etc/letsencrypt/live/goodtoeatfoods.com/fullchain.pem ssl/goodtoeatfoods.com.crt
sudo cp /etc/letsencrypt/live/goodtoeatfoods.com/privkey.pem ssl/goodtoeatfoods.com.key
sudo chmod 644 ssl/goodtoeatfoods.com.crt
sudo chmod 600 ssl/goodtoeatfoods.com.key
```

### Step 6: Update nginx.conf

Update the SSL certificate paths in `nginx.conf` if needed (they should already be correct).

### Step 7: Deploy

```bash
# Make deploy script executable
chmod +x deploy.sh

# Run deployment
./deploy.sh
```

### Step 8: Set Up Auto-Renewal for SSL

```bash
# Add cron job for SSL renewal
sudo crontab -e
# Add this line:
0 0 * * * certbot renew --quiet && docker-compose -f /opt/GoodToEat/docker-compose.yml restart nginx
```

## Option 2: Deploy to Streamlit Cloud with Custom Domain

### Step 1: Deploy to Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Select repository: `mohini-workday/GoodToEat`
5. Branch: `main`
6. Main file: `app.py`
7. Click "Deploy"

### Step 2: Configure Custom Domain

1. In your Streamlit Cloud dashboard, go to your app's settings
2. Click on "Custom domain"
3. Enter: `goodtoeatfoods.com`
4. Follow the DNS configuration instructions provided by Streamlit
5. Add the required DNS records in your domain provider

**Note:** Streamlit Cloud custom domain feature may require a paid plan.

## Option 3: Deploy to Cloud Platforms

### AWS (EC2 + Elastic Beanstalk or ECS)

1. Create an EC2 instance
2. Follow Option 1 steps
3. Or use AWS Elastic Beanstalk with Docker

### Google Cloud Platform

1. Use Cloud Run with Docker
2. Or use Compute Engine and follow Option 1

### DigitalOcean

1. Create a Droplet
2. Follow Option 1 steps
3. Or use App Platform with Dockerfile

### Heroku

1. Install Heroku CLI
2. Create `Procfile`:
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```
3. Deploy:
   ```bash
   heroku create goodtoeatfoods
   heroku config:set STREAMLIT_SERVER_PORT=$PORT
   git push heroku main
   ```

## Monitoring and Maintenance

### Check Application Status

```bash
docker-compose ps
docker-compose logs -f streamlit-app
```

### Update Application

```bash
cd /opt/GoodToEat
git pull origin main
./deploy.sh
```

### Backup

```bash
# Backup images
tar -czf backup-$(date +%Y%m%d).tar.gz Images/
```

## Troubleshooting

### App Not Loading

1. Check if containers are running: `docker-compose ps`
2. Check logs: `docker-compose logs`
3. Verify DNS: `nslookup goodtoeatfoods.com`
4. Check firewall: Ensure ports 80 and 443 are open

### SSL Certificate Issues

1. Verify certificate paths in nginx.conf
2. Check certificate expiration: `sudo certbot certificates`
3. Renew if needed: `sudo certbot renew`

### Port Conflicts

If port 8501 is in use, update `docker-compose.yml` to use a different port.

## Support

For deployment issues, check:
- Docker logs: `docker-compose logs`
- Nginx logs: `docker logs goodtoeat-nginx`
- Streamlit logs: `docker logs goodtoeat-streamlit`

## Security Notes

1. Keep your server updated: `sudo apt update && sudo apt upgrade`
2. Use strong passwords and SSH keys
3. Enable firewall: `sudo ufw enable`
4. Regularly renew SSL certificates
5. Monitor application logs for errors

