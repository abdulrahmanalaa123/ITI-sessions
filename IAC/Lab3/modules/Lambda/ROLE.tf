
resource "aws_lambda_permission" "allow_bucket" {
  statement_id  = "AllowExecutionFromS3Bucket"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.email_func.arn
  principal     = "s3.amazonaws.com"
  source_arn    = data.aws_s3_bucket.state_bucket.arn
}

# resource "aws_iam_role" "iam_for_s3" {
#   name               = "iam_for_s3"
#   assume_role_policy = data.aws_iam_policy_document.allow_bucket.json
# }

data "aws_iam_policy_document" "access_notifcations" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }

    actions = [ "ses:SendEmail","ses:SendRawEmail"]
  }
}

resource "aws_iam_role" "iam_for_lambda_emails" {
  name               = "iam_for_lambda_emails"
  assume_role_policy = data.aws_iam_policy_document.access_notifcations.json
}
