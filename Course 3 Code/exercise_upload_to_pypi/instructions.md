# Upload a package to Pypi

1. Run in terminal
   ```bash
   python3 setup.py sdist
   ```
   Sẽ tạo ra hai folders. Trong folders `dist`, file `hieu_distribtuions-0.1.tar.gz` sẽ là file ta up lên Pypi 
   repository.
2. Install package
   ```bash
   pip install twine
   ```
3. Upload package to test Pipy
   ```bash
   twine upload --repository-url https://test.pypi.org/legacy/ dist/*
   ```
4. Thử install package vừa up
   ```bash
   pip install -i https://test.pypi.org/simple/ hieu-distributions
   ```
5. Nếu ổn rồi thì upload to Pipy
   ```bash
   twine upload dist/*
   ```