#include <iostream>
using namespace std;

int main() {
  // Deklarasi dan inisialisasi array
  int arr[6] = {64, 34, 25, 12, 22, 11};
  int n = sizeof(arr) / sizeof(arr[0]); // Ukuran array

  // Tampilan array sebelum diurutkan
  cout << "Array sebelum diurutkan: ";
  for (int i = 0; i < n; i++) {
    cout << arr[i] << " ";
  }

  // Algoritma bubble sort
  for (int i = 0; i < n - 1; i++) {
    for (int j = 0; j < n - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        swap(arr[j], arr[j + 1]);
      }
    }
  }

  // Tampilan array setelah diurutkan
  cout << "\nArray setelah diurutkan: ";
  for (int i = 0; i < n; i++) {
    cout << arr[i] << " ";
  }

  return 0;
}