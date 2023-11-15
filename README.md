## Cracker9000, a Python Password Cracker
### 2023 CLHS Cybersecurity

### Rubric (46/51)
- [x] Usage of GitHub (3)
- [x] Load 10,000 most common passwords (4)
- [x] Brute force cracking (10)
- [x] Dictionary cracking (10)
- [x] Can run via command line with arguments (4)
- [x] MD5 hashed passwords can be checked (5)
- [x] SHA-256 hashed passwords can be checked (5)
- [ ] BCrypt hashed passwords can be checked (5)
- [x] Includes README.md (1)

### Modes/Command Line Arguments:
  - (None) = Default Setting, Prompt
  - 0 = Change password
  - 1 = Dictionary Cracking
  - 2 = Brute Force Cracking
  - 3 = Convert to MD5
  - 4 = Convert to SHA256
  - 6 = Quit

### Formatting:
  `python3 masterCrack.py`
  `python3 masterCrack.py 1`
  `python3 masterCrack.py 2`

### Dependencies:
`sys`
`hashlib`
`BCrypt`
