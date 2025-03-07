module "lambda" {
  source       = "./modules/Lambda"
  region       = var.region
  bucket_name  = "state-bucket-tomato"
  source_email = "abdulrahmanalaa497@gmail.com"
  recipients   = "abdulrahmanalaa22@gmail.com"
}