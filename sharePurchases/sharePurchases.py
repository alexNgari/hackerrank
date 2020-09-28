import re
investments = 'ABBCZBAC'

pattern = re.compile(r'''([D-Z]*A[AD-Z]*B[ABD-Z]*C[A-Z]*)|
                        ([D-Z]*B[BD-Z]*A[BAD-Z]*C[A-Z]*)|
                        ([D-Z]*B[BD-Z]*C[BCD-Z]*A[A-Z]*)|
                        ([D-Z]*A[AD-Z]*C[ACD-Z]*B[A-Z]*)|
                        ([D-Z]*C[CD-Z]*A[CAD-Z]*B[A-Z]*)|
                        ([D-Z]*C[CD-Z]*B[CBD-Z]*A[A-Z]*)''')

