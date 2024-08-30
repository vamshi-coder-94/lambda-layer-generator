import os
import subprocess
import zipfile
import shutil
import argparse

def create_virtualenv(venv_dir):
    subprocess.run(['python3', '-m', 'venv', venv_dir], check=True)

def install_libraries(venv_dir, libraries):
    subprocess.run([os.path.join(venv_dir, 'bin', 'pip'), 'install'] + libraries, check=True)

def create_layer_zip(venv_dir, output_file):
    site_packages_dir = os.path.join(venv_dir, 'lib', 'python3.12', 'site-packages')
    layer_dir = os.path.join('python', 'lib', 'python3.12', 'site-packages')
    
    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, _, files in os.walk(site_packages_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path, os.path.join(layer_dir, os.path.relpath(file_path, site_packages_dir)))

def main():
    parser = argparse.ArgumentParser(description='Generate an AWS Lambda Layer for specified libraries.')
    parser.add_argument('libraries', metavar='L', type=str, nargs='+', help='a list of libraries to include in the AWS Lambda Layer')
    args = parser.parse_args()

    libraries = args.libraries
    venv_dir = '.venv'
    output_file = 'lambda-layer.zip'

    # Create virtual environment
    create_virtualenv(venv_dir)

    # Install the specified libraries
    install_libraries(venv_dir, libraries)

    # Create the zip file for the Lambda Layer
    create_layer_zip(venv_dir, output_file)

    # Clean up the virtual environment
    shutil.rmtree(venv_dir)

    print(f'Lambda Layer for {", ".join(libraries)} created: {output_file}')

if __name__ == '__main__':
    main()