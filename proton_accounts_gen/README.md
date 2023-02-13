# proton_generator.py

Script uses Selenium to auto-generate free Proton VPN accounts (verification needed).

Verification: 

    - First it asks for Captcha
    - Then they ask you for e-mail verification (10min mail works)
    - After few verifications, there is only SMS verification available

Script will wait for verification to complete.

## Usage of proton_generator.py

Script needs a geckodriver installed.

```python3
python3 proton+generator.py
Enter a number of accounts needed: X #X is a number
```
And make a verification!