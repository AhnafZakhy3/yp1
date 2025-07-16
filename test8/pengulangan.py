def menampilkan_deret_bilangan_prima(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    deret = [i for i in range(2, n+1) if is_prime(i)]
    return deret

n = 100  # contoh nilai n
print(menampilkan_deret_bilangan_prima(n))