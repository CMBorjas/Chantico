# Project Chantico: The Digital Hearth Guardian

Chantico is a locally-hosted, unrestricted AI agent designed to act as a "Digital Guardian" for home networks. Named after the Aztec goddess of the hearth and domestic fire, Chantico protects the "homestead" by monitoring network traffic, managing hardware, and securing sensitive digital assets.

## 1. Vision & Architecture
Chantico is built to be a collaborative security partner. It integrates with **OPNsense** and **TPLink** to provide real-time analysis and moves from a recommendation-based model to full autonomous control once a 99% reliability threshold is met.

### System Stack:
* **Model Host:** Ollama (Local) or any other LLM provider
* **Orchestration:** CrewAI / Custom Python Logic 
* **Interface:** Android SDK (Kotlin/Jetpack Compose)
* **Infrastructure:** Docker Compose / Kubernetes (for future production scaling)
* **Network Core:** OPNsense Firewall

## 2. Key Features
* **OPNsense Integration:** Continuous monitoring of firewall logs and traffic patterns.
* **Hardware Management:** Direct interaction with managed switches to VLAN-isolate suspicious devices.
* **Blunder Prevention:** Acts as a "sanity check" for networking configurations, flagging errors that could lead to security holes.
* **Asset Protection:** Specific focus on securing IoT clusters, home media servers, and encrypted documentation.
* **Self-Improving Defense:** Designed to analyze OPNsense source code to identify and patch vulnerabilities.
* **Network Scanning:**  Designed to scan the network for new devices and identify them.

## 3. Installation (Local Development)
1.  **Clone the Repository:**
    `git clone https://github.com/CMBORJAS/chantico.git`
    Not yet implemented, but will be needed for the project.
2.  **Spin up the Backend:**
    `docker-compose up -d` (Includes Ollama and the Agent Router)
3.  **Configure OPNsense:**
    Enable syslog forwarding to the Chantico container IP.
4.  **Mobile Link:**
    Build and install the Android APK from the `/mobile` directory. Ensure connection via **Secure Tunnel/VPN** for remote access.

## 4. The Trust Roadmap
* **Phase 1 (Current):** Observation & Recommendation. Chantico flags anomalies and suggests OPNsense rules.
* **Phase 2:** Collaborative Debugging. Chantico identifies user "blunders" in real-time.
* **Phase 3:**  Mobile app development and integration with the backend.
* **Phase 4:** Full Autonomy. Upon reaching >99% reliability, Chantico assumes full control over firewall rules and switch port management.