from utils.common_utils import generate_random_email

def test_generate_random_email():
    email = generate_random_email()
    print("Generated email:", email)
    assert email.startswith("testuser")
    assert email.endswith("@example.com")

from utils.logger import get_logger

logger = get_logger(__name__)



   