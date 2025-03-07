data "aws_s3_bucket" "state_bucket" {
  bucket = var.bucket_name
}

resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = data.aws_s3_bucket.state_bucket.id

  lambda_function {
    lambda_function_arn = aws_lambda_function.email_func.arn
    events              = ["s3:ObjectCreated:*","s3:ObjectRemoved:*"]
    # should add a filter_prefix if i specifically need certain environments 
    filter_suffix = ".tfstate"
  }

  depends_on = [aws_lambda_permission.allow_bucket]
}