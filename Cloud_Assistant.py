import streamlit as st
import replicate
import os

# App title
st.set_page_config(page_title="☁️💬 Google Cloud's Nuvola Chatbot")
sidebar_logo = 'res\googlecloudslidebar.png'
main_body_logo = 'res\googlecloudmain.png'
st.logo(sidebar_logo, icon_image=main_body_logo)
st.header('Nuvola Chatbot',divider='rainbow')

# Replicate Credentials
with st.sidebar:
    st.header('☁️💬 Google Cloud\'s Nuvola Chatbot',divider='rainbow')
    if 'REPLICATE_API_TOKEN' in st.secrets:
        st.success('API key already provided!', icon='✅')
        replicate_api = st.secrets['REPLICATE_API_TOKEN']
    else:
        replicate_api = st.text_input('Enter Replicate API token:', type='password')
        if not (replicate_api.startswith('r8_') and len(replicate_api)==40):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')
    os.environ['REPLICATE_API_TOKEN'] = replicate_api

    st.subheader('Models and parameters')
    selected_model = st.sidebar.selectbox('Choose a Llama2 model', ['Llama2-7B', 'Llama2-13B'], key='selected_model')
    if selected_model == 'Llama2-7B':
        llm = 'a16z-infra/llama7b-v2-chat:4f0a4744c7295c024a1de15e1a63c880d3da035fa1f49bfd344fe076074c8eea'
    elif selected_model == 'Llama2-13B':
        llm = 'a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5'
    temperature = st.sidebar.slider('Temperature', min_value=0.01, max_value=5.0, value=0.1, step=0.01)
    top_p = st.sidebar.slider('Top-P', min_value=0.01, max_value=1.0, value=0.9, step=0.01)
    max_length = st.sidebar.slider('Max length', min_value=32, max_value=128, value=120, step=8)

# Predefined context
context = """Google Cloud Platform (GCP), offered by Google, is a suite of cloud computing services that provides a series of modular cloud services including computing, data storage, data analytics, and machine learning, alongside a set of management tools. It runs on the same infrastructure that Google uses internally for its end-user products, such as Google Search, Gmail, and Google Docs, according to Verma, et.al. Registration requires a credit card or bank account details.

Google Cloud Platform provides infrastructure as a service, platform as a service, and serverless computing environments.

In April 2008, Google announced App Engine, a platform for developing and hosting web applications in Google-managed data centers, which was the first cloud computing service from the company. The service became generally available in November 2011. Since the announcement of App Engine, Google added multiple cloud services to the platform.

Google Cloud Platform is a part of Google Cloud, which includes the Google Cloud Platform public cloud infrastructure, as well as Google Workspace (G Suite), enterprise versions of Android and ChromeOS, and application programming interfaces (APIs) for machine learning and enterprise mapping services.

Cloud computing, according to Google Cloud Platform (GCP), refers to the delivery of computing services—including computing power, storage, databases, networking, software, and analytics—over the internet ("the cloud") to offer faster innovation, flexible resources, and economies of scale. Google Cloud Platform provides a robust infrastructure and a wide range of services that enable businesses to leverage these advantages efficiently.

Products:
Google lists over 100 products under the Google Cloud brand. Some of the key services are listed below.

1.Compute:
App Engine – Platform as a Service to deploy applications developed with Java, PHP, Node.js, Python, C#, .Net, Ruby and Go programming languages.

Compute Engine – Infrastructure as a Service to run Microsoft Windows and Linux virtual machines.

Google Kubernetes Engine (GKE) or GKE on-prem offered as part of Anthos platform[6][7] – Containers as a Service based on Kubernetes.

Cloud Functions – Functions as a Service to run event-driven code written in Node.js, Java, Python, or Go.

Cloud Run – Compute execution environment based on Knative.[8] Offered as Cloud Run (fully managed)[9] or as Cloud Run for Anthos.[9] Currently supports GCP, AWS and VMware management.[10]


2.Storage and databases:
Cloud Storage – Object storage with integrated edge caching to store unstructured data.

Cloud SQL – Database as a Service based on MySQL, PostgreSQL and Microsoft SQL Server.

Cloud Bigtable – Managed NoSQL database service.[11]

Cloud Spanner – Horizontally scalable, strongly consistent, relational database service.[12]

Cloud Datastore – NoSQL database for web and mobile applications.[13]

Persistent Disk – Block storage for Compute Engine virtual machines.[14]

Cloud Memorystore – Managed in-memory data store based on Redis and Memcached.[15]

Local SSD: High-performance, transient, local block storage.

Filestore: High-performance file storage for Google Cloud users.[16]

AlloyDB: Fully managed PostgreSQL database service.[17]


3.Networking:
VPC – Virtual Private Cloud for managing the software defined network of cloud resources.

Cloud Load Balancing – Software-defined, managed service for load balancing the traffic.

Cloud Armor – Web application firewall to protect workloads from DDoS attacks.

Cloud CDN – Content Delivery Network based on Google's globally distributed edge points of presence.

Cloud Interconnect – Service to connect a data center with Google Cloud Platform

Cloud DNS – Managed, authoritative DNS hosting service running on the same infrastructure as Google.

Network Service Tiers – Option to choose Premium vs Standard network tier for higher-performing network.


4.Big data:
BigQuery – Scalable, managed enterprise data warehouse for analytics.[18]

Cloud Dataflow – Managed service based on Apache Beam for stream and batch data processing.[19]

Cloud Data Fusion – A managed ETL service based on the Open Source Cask Data Application Platform.[20]

Dataproc – Big data platform for running Apache Hadoop and Apache Spark jobs.[21]

Cloud Composer – Managed workflow orchestration service built on Apache Airflow.[22]

Cloud Datalab – Tool for data exploration, analysis, visualization and machine learning. This is a fully managed Jupyter Notebook service.[23]

Cloud Dataprep – Data service based on Trifacta to visually explore, clean, and prepare data for analysis.[24]

Cloud Pub/Sub – Scalable event ingestion service based on message queues.[25]

Looker Studio – Business intelligence tool to visualize data through dashboards and reports.[26]

Looker – Business intelligence platform.[27][28]


5.Cloud AI:
Cloud AutoML – Service to train and deploy custom machine learning models. As of September 2018, the service is in Beta.[29]

Cloud TPU – Accelerators used by Google to train machine learning models.[30]

Cloud Machine Learning Engine – Managed service for training and building machine learning models based on mainstream frameworks.[31]

Cloud Talent Solution (formerly Cloud Job Discovery) – Service based on Google's search and machine learning capabilities for the recruiting ecosystem.[32]

Dialogflow Enterprise – Development environment based on Google's machine learning for building conversational interfaces.[33]

Cloud Natural Language – Text analysis service based on Google Deep Learning models.[34]

Cloud Speech-to-Text – Speech to text conversion service based on machine learning.[35]

Cloud Text-to-Speech – Text to speech conversion service based on machine learning.[36]

Cloud Translation API – Service to dynamically translate between thousands of available language pairs.

Cloud Vision API – Image analysis service based on machine learning.[37]

Cloud Video Intelligence – Video analysis service based on machine learning.[38]


6.Management tools:
Operations suite (formerly Stackdriver ) – Monitoring, logging, tracing, and diagnostics for applications on Google Cloud Platform.[39]

Cloud Deployment Manager  - Tool to deploy Google Cloud Platform resources defined in templates created in YAML, Python or Jinja2.[40]

Cloud Console – Web interface to manage Google Cloud Platform resources.

Cloud Shell – Browser-based shell command-line access to manage Google Cloud Platform resources.

Cloud Console Mobile App – Android and iOS application to manage Google Cloud Platform resources.

Cloud APIs – APIs to programmatically access Google Cloud Platform resources


7.Identity and security:
Cloud Identity – Single sign-on (SSO) service based on SAML 2.0 and OpenID.

Cloud IAM – Identity & Access Management (IAM) service for defining policies based on role-based access control.

Cloud Identity-Aware Proxy – Service to control access to cloud applications running on Google Cloud Platform without using a VPN.

Cloud Data Loss Prevention API – Service to automatically discover, classify, and redact sensitive data.

Security Key Enforcement – Two-step verification service based on a security key.

Cloud Key Management Service – Cloud-hosted key management service integrated with IAM and audit logging.

Cloud Resource Manager – Service to manage resources by project, folder, and organization based on the hierarchy.

Cloud Security Command Center – Security and data risk platform for data and services running in Google Cloud Platform.

Cloud Security Scanner – Automated vulnerability scanning service for applications deployed in App Engine.

Access Transparency – Near real-time audit logs providing visibility to Google Cloud Platform administrators.

VPC Service Controls – Service to manage security perimeters for sensitive data in Google Cloud Platform services.

8.Internet of things (IoT):
Cloud IoT Core – Secure device connection and management service for Internet of Things.

Edge TPU – Purpose-built ASIC designed to run inference at the edge. As of September 2018, this product is in private beta.

Cloud IoT Edge – Brings AI to the edge computing layer.

9.API platform:
Maps Platform – APIs for maps, routes, and places based on Google Maps.

Apigee API Platform – Lifecycle management platform to design, secure, deploy, monitor, and scale APIs.

API Monetization – Tool for API providers to create revenue models, reports, payment gateways, and developer portal integrations.

Developer Portal – Self-service platform for developers to publish and manage APIs.

API Analytics – Service to analyze API-driven programs through monitoring, measuring, and managing APIs.

Apigee Sense – Enables API security by identifying and alerting administrators to suspicious API behaviors.

Cloud Endpoints – An NGINX-based proxy to deploy and manage APIs.

Service Infrastructure – A set of foundational services for building Google Cloud products.


Google Cloud Platform (GCP) operates on several key principles that guide its design, operation, and service offerings. These principles are fundamental to understanding how Google Cloud provides reliability, scalability, and security to its users:
1. Security First Approach:
Google Cloud Platform prioritizes security across its infrastructure, services, and operations. Key aspects of its security-first approach include:
Built-in Security: Security features such as encryption at rest and in transit, IAM (Identity and Access Management), and network security policies are built into every layer of GCP services.
Compliance and Certifications: GCP adheres to industry standards and certifications (e.g., ISO 27001, SOC 2, PCI DSS) to ensure data protection and regulatory compliance.
Continuous Monitoring and Protection: Google employs advanced threat detection, anomaly detection, and incident response mechanisms to monitor and protect its infrastructure and customer data.

2. Global Infrastructure:
Google Cloud operates on a global network of data centers strategically distributed around the world. Key aspects of its global infrastructure include:
Availability Zones and Regions: GCP divides its infrastructure into regions (geographical locations) and availability zones (physically separate locations within regions) to provide redundancy and fault tolerance.
Edge Locations: Google's extensive network of edge locations and points of presence (PoPs) ensures low-latency access to services and data for users globally.

3. Scalability and Flexibility:
GCP is designed to scale seamlessly to meet the evolving needs of businesses. Key scalability and flexibility principles include:
Elastic Compute Resources: Services like Compute Engine and Kubernetes Engine enable businesses to scale compute resources up or down based on demand without downtime.
Managed Services: GCP offers fully managed services (e.g., Cloud SQL, BigQuery) that automatically scale to handle workload fluctuations and peak demands.
Serverless Computing: Products like Cloud Functions and App Engine allow developers to focus on writing code without worrying about infrastructure management, enabling rapid deployment and scaling.

4. Openness and Hybrid Cloud:
Google Cloud embraces an open approach, supporting a wide range of operating systems, programming languages, frameworks, and tools. Key aspects include:
Multi-Cloud and Hybrid Cloud Solutions: GCP provides solutions for connecting on-premises infrastructure with cloud resources (e.g., Anthos), facilitating hybrid cloud deployments.
Interoperability: GCP services integrate with popular open-source technologies and third-party tools, promoting interoperability and flexibility for developers and IT teams.

5. Innovation and Sustainability:
Google Cloud is committed to continuous innovation and sustainability. Key principles include:
Advanced Technologies: Investment in cutting-edge technologies such as artificial intelligence (AI), machine learning (ML), and data analytics to drive innovation and business transformation.
Environmental Responsibility: Google Cloud is committed to sustainability, striving for energy efficiency, reducing carbon footprint, and supporting renewable energy initiatives across its data centers.

6. Reliability and Resilience:
Google Cloud Platform is engineered to deliver high availability, reliability, and resilience. Key principles include:
Redundancy and Failover: Services are designed with redundancy and failover mechanisms across multiple availability zones and regions to minimize service interruptions.
SLAs (Service Level Agreements): GCP provides SLAs for uptime and performance for its core services, ensuring reliability and accountability.

"""

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Hello 👋, I am Nuvola , How may I assist you today?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "Hello 👋, I am Nuvola ,How may I assist you today?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

# Function for generating LLaMA2 response
def generate_llama2_response(prompt_input):
    string_dialogue = "You are a helpful assistant of Google Cloud. You are named as 'Nuvola' meaning Cloud in Italian. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'.\n\n Your response should always be in context related to Google Cloud. Use the following context to answer questions:\n\n" + context + "\n\n"
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            string_dialogue += "User: " + dict_message["content"] + "\n\n"
        else:
            string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"
    output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5', 
                           input={"prompt": f"{string_dialogue} {prompt_input} Assistant: ",
                                  "Temperature":temperature, "Top-P":top_p, "Max length":max_length, "repetition_penalty":1})
    return output

# User-provided prompt
if prompt := st.chat_input(disabled=not replicate_api):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_llama2_response(prompt)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message) 