import hashlib

def generate_hash_pdf_md5(pdf_file):
    hash_md5 = hashlib.md5()
    with open(pdf_file,'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def generate_hash_pdf_sha256(pdf_file):
    hash_sha256 = hashlib.sha256()
    with open(pdf_file,'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

if __name__ == "__main__":
    pdf_file = "sample.pdf"
    hash_md5 = generate_hash_pdf_md5(pdf_file)
    hash_sha256 = generate_hash_pdf_sha256(pdf_file)
    print(f"MD5 hash for {pdf_file}: {hash_md5}")
    print(f"SHA256 hash for {pdf_file}: {hash_sha256}")
  