import os
import time
import random
import string
from datetime import datetime


class StoragePerformanceTest:
    def __init__(self, test_dir="./test_data"):
        self.test_dir = test_dir
        self.ensure_directory()

    def ensure_directory(self):
        """テストディレクトリが存在することを確認"""
        os.makedirs(self.test_dir, exist_ok=True)

    def generate_random_data(self, size_mb):
        """指定サイズのランダムデータを生成"""
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(size_mb * 1024 * 1024)).encode()

    def write_test(self, file_size_mb, num_files, cache_random_data=True):
        """書き込みパフォーマンステスト"""
        total_time = 0
        total_size = 0

        print(f"\n=== 書き込みパフォーマンステスト ===")
        print(f"ファイルサイズ: {file_size_mb}MB")
        print(f"ファイル数: {num_files}")

        for i in range(num_files):
            if not cache_random_data or i == 0:
                print("Start generating random data")
                data = self.generate_random_data(file_size_mb)
                print("Random data generated")

            file_path = os.path.join(self.test_dir, f'test_file_{i}.dat')

            start_time = time.time()
            with open(file_path, 'wb') as f:
                f.write(data)
            end_time = time.time()

            write_time = end_time - start_time
            total_time += write_time
            total_size += file_size_mb

            print(f"ファイル {i + 1}: {file_size_mb}MB 書き込み完了 - {write_time:.2f}秒")

        avg_speed = (total_size / total_time) if total_time > 0 else 0
        print(f"\n=== 結果 ===")
        print(f"総書き込みサイズ: {total_size}MB")
        print(f"総書き込み時間: {total_time:.2f}秒")
        print(f"平均書き込み速度: {avg_speed:.2f}MB/秒")

        return {
            'total_size': total_size,
            'total_time': total_time,
            'avg_speed': avg_speed
        }

    def cleanup(self):
        """テストファイルの削除"""
        for file in os.listdir(self.test_dir):
            if file.startswith('test_file_'):
                os.remove(os.path.join(self.test_dir, file))


def main():
    # テストパラメータ
    FILE_SIZE_MB = 100  # 各ファイルのサイズ
    NUM_FILES = 5  # テストするファイル数

    # テストの実行
    test = StoragePerformanceTest()
    try:
        print(f"ストレージパフォーマンステスト開始: {datetime.now()}")
        results = test.write_test(FILE_SIZE_MB, NUM_FILES)
        print(f"\nテスト完了: {datetime.now()}")
    finally:
        test.cleanup()


if __name__ == "__main__":
    main()