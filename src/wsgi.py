import subprocess

def run_streamlit_app():
    command = "streamlit run src/app.py"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    run_streamlit_app()