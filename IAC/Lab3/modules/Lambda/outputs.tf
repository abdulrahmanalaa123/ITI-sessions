output "bucket" {
  value = data.aws_s3_bucket.state_bucket
}
output "lambda_func" {
  value = aws_lambda_function.email_func
}