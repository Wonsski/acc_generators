# proton_generator.py

Script uses Selenium to auto-generate free Proton (VPN, Mail etc.) accounts (verification needed).

Verification (change IP to have only captcha): 

    - First it asks for Captcha
    - Then they ask you for e-mail verification (10min mail works)
    - After few verifications, there is only SMS verification available

Script will wait for verification to complete.

## Usage of proton_generator.py

Script needs a geckodriver installed.

```python3
python3 proton_generator.py [N - Number of accounts to generate, default 10]

#example
python3 proton_generator.py 7 #Will generate 7 accounts
```
And make a verification!