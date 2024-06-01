from django.core.validators import RegexValidator




MOBILE_REGEX = RegexValidator(regex='^(?!0|1|2|3|4|5)(\d)(?!\1+$)\d{9}$', message='Enter valid mobile number.')