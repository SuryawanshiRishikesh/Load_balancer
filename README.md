**Nginx Load Balancer with Python Backend Servers**
This project demonstrates the setup of a robust Nginx-based load balancer with Python backend servers. The load balancer uses Nginx to distribute traffic among three Python servers, ensuring high availability and efficient traffic management. This setup is enhanced with security hardening, logging, monitoring, and health checks to make it production-ready.

**Features:**
1. Load Balancing:
Implements a round-robin load balancing algorithm to evenly distribute traffic across three Python backend servers.
2. Health Checks:
Periodically checks the availability of backend servers to avoid routing traffic to offline or unresponsive servers.
3. Custom Logging:
Configured Nginx to log detailed information for access and error logs in a custom format.
4. Security Hardening:
Implements security headers to mitigate common vulnerabilities like XSS and clickjacking.
5. Ease of Monitoring:
Configured logs can be tailed for real-time monitoring.

**Installation and Setup**

Prerequisites:
Linux-based operating system (tested on Ubuntu)
Python 3.6+ installed
Nginx installed

**Steps:**
1) Clone the Repository:

git clone https://github.com/your-username/LB_Project.git
cd LB_Project

2) Set Up Python Servers: Navigate to each server directory and start the servers:

cd Servers/Server1
python3 server1.py
Repeat for Server2 and Server3.

3) Configure Nginx: Copy the Nginx configuration files:

sudo cp nginx.conf /etc/nginx/
sudo cp load_balancer.conf /etc/nginx/conf.d/

4) Restart Nginx:

sudo systemctl restart nginx
Access the Load Balancer: Open your browser and navigate to http://<your-vm-ip>.

**Usage**
i) Monitor Logs:

sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log
Check Backend Health: Health checks automatically mark unresponsive servers as offline in the load balancer.

ii) Restart Nginx:

sudo systemctl restart nginx
Access the Load Balancer: Open your browser and navigate to http://<your-vm-ip>.

**Future Enhancements**
SSL/TLS Termination: Enable HTTPS for secure communication.
Advanced Monitoring: Integrate tools like Prometheus and Grafana.
Rate Limiting: Prevent abusive traffic from overwhelming the servers.
