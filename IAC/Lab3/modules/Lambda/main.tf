data "archive_file" "lambda" {
  type        = "zip"
  source_file = "lambda.py"
  output_path = "lambda_function_payload.zip"
}

resource "aws_lambda_function" "email_func" {
  filename      = "lambda_function_payload.zip"
  function_name = "email_on_change"
  role          = aws_iam_role.iam_for_lambda_emails.arn
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.9"
  environment {
        variables = {
          "SOURCE" = var.source_email
          "REGION" = "eu-central-1"
          "RECIPIENT" = var.recipients
        }
  }
}
