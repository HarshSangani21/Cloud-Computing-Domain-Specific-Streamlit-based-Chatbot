# Nuvola Chatbot

## Overview
The **Nuvola Chatbot** is a Streamlit-based application designed to simulate a helpful assistant for Google Cloud Platform (GCP). Leveraging the Replicate API and LLaMA2 models, it provides a conversational interface to help users get information and answers related to Google Cloud Platform (GCP) services and products.

## Features
- **Streamlit UI**: Interactive and user-friendly interface.
- **Model Selection**: Choose between different LLaMA2 models (7B and 13B parameters).
- **Customizable Parameters**: Adjust temperature, top-p, and max length for model responses.
- **Chat History**: Persistent chat history that can be cleared via a button.
- **Contextual Responses**: Responses are based on a predefined GCP context.

## Prerequisites

Before running this application, ensure you have the following:

- **Python** [3.8](https://www.python.org/downloads/release/python-3819/) or later.
- **Streamlit**.
- **Replicate**.
- **API Token of Replicate**.
  
## Instructions

### Setup Installation

1. **Install Dependencies**:

    ```bash
    pip install streamlit replicate
    ```

2. **Set Up Replicate API Token**:

    - Obtain an API token from [Replicate](https://replicate.com/).
    - Save the token in a `.streamlit/secrets.toml` file or enter it directly in the app interface.

### Configuration

1. **Run the Application**:

    ```bash
    streamlit run Cloud_Assistant.py
    ```

2. **Access the Application**:

   Streamlit will automatically open the web-application in default browser.

   *OR* Open your web browser and go to `http://localhost:8501`.

3. **Configure Chatbot Settings**:

    - **API Token**: Enter Replicate API token in the slidebar.
    - **Model Selection**: Choose between `Llama2-7B` and `Llama2-13B`.
    - **Temperature**: Adjust to control the randomness of responses.
    - **Top-P**: Modify to control the diversity of responses.
    - **Max Length**: Set the maximum length for generated responses.

## File Structure
- `Cloud_Assistant.py`: Main application script.
- `res/`: Directory containing images for logos.
- `.streamlit/`: Directory containing `secrets.toml` file for using API tokens saved in it. `config.toml` configures the streamlit application.

## Help

For help with the project, users can:

- **Open an Issue**: Report bugs or request features on the project's GitHub issue tracker.
- **Contact the Maintainer**: Reach out to the project maintainer for direct support.

### Maintainer

This project is maintained by Harsh Sangani [hharshsangani@gmail.com ]. Contributions are welcome from the community.


## Acknowledgements
- **Streamlit**: For the interactive web app framework.
- **Replicate**: For providing the API to interact with LLaMA2 models.
- **Google Cloud Platform**: For the extensive resources and tools available on the platform.
- **DJS InfoMatrix**: For the Guidance on this project.
- **Wikipedia**: For the content and information.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this project as long as you include the original license. For more details, see the [LICENSE](LICENSE) file.

---

Feel free to reach out for any further assistance or contributions. Happy coding!
