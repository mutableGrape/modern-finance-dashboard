# Modern Finance Dashboard

A sweet and simple streamlit app for monitoring your personal finances. Input your data as a CSV, and optionally attach a local LLM to plot your spending, analyse your habits, and get advice on how to use your finances strategically. 

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/my-streamlit-app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd my-streamlit-app
   ```

3. Install the project dependencies using Poetry:

   ```bash
   poetry install
   ```

## Usage

1. Run the Streamlit app:

   ```bash
   poetry run streamlit run src/app.py
   ```

2. Open your web browser and go to `http://localhost:8501` to view the app.

## Dataset

The app uses a sample dataset located at `src/data/sample_data.csv`. You can modify this file or replace it with your own dataset.

## Dependencies

The project dependencies are managed using Poetry. The `pyproject.toml` file specifies the required packages and their versions. The `poetry.lock` file contains the resolved versions of the dependencies.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
```
This file is intentionally left blank.
```