from moto import mock_sts, mock_s3


@mock_sts()
@mock_s3()
def test_put_delete_s3_object(app):
    from lemur.plugins.lemur_aws.s3 import put, delete, get

    data = "dummy data"
    put(bucket_name="public-bucket",
        prefix="some_path/foo",
        data=data,
        encrypt=None,
        account_number="123456789012")

    response = get(bucket_name="public-http01-validator-test",
                   prefix="some_path/foo",
                   account_number="123456789012")
    assert (response == data)

    delete(bucket_name="public-bucket",
           prefix="some_path/foo",
           account_number="123456789012")

    response = get(bucket_name="public-http01-validator-test",
                   prefix="some_path/foo",
                   account_number="123456789012")
    assert (response != data)
