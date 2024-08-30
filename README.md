# AWS Lambda Layer Generator

This Python script generates an AWS Lambda Layer for specified libraries. The generated layer includes the specified libraries and their dependencies, packaged in the correct structure for AWS Lambda.

## Prerequisites

- Python 3.12 or later
- `pip` (Python package installer)

## Usage

1. **Clone the repository or download the script:**

   ```sh
   git clone <repository-url>
   cd <repository-directory>

2. Run the script with desired libraries:

   ```sh
   python3 generate_lambda_layer.py <library1> <library2> ...
   ```

   For example:

   ```sh
   python3 generate_lambda_layer.py requests
   ```

   The script will generate a ZIP file named `lambda_layer.zip` in the current directory.
   The ZIP file contains the specified libraries and their dependencies, packaged in the correct structure for AWS Lambda.