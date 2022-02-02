#include <iostream>
#include <assert.h>
using namespace std;


class DynamicArray {

    int *array;
    int capacity = 2;
    int size;

public:
    DynamicArray() {
        array = new int[capacity];
        size = 0;
    }

    void append(int element) {
        insertAt(element, size);
    }

    int length() {
        return size;
    }

    int get(int pos) {
        return array[pos];
    }

    ~DynamicArray() {
        delete[] array;
    }

private:
    void insertAt(int element, int pos) {
        assert(0 <= pos && pos <= size);
        if(size == capacity) {
            resize();
        }
        for(int i = size; i > pos; i--) {
            array[i] = array[i-1];
        }
        size++;
        array[pos] = element;
    }

    void resize() {
        capacity *= 2;
        int *temp = new int[capacity];
        copy(array, array + size, temp);
        delete [] array;
        array = temp;
    }

};

class DynamicArrayWithStats : public DynamicArray {
public:
    int max(){
        int max = get(0);
        for (int i = 1; i < length(); i++){
            if (get(i) > max)
                max = get(i);
        }
        return max;
    }
    int min(){
        int min = get(0);
        for (int i = 1; i < length(); i++){
            if (get(i) < min)
                min = get(i);
        }
        return min;
    }
    int mean(){
        int sum = 0;
        for (int i = 0; i < length(); i++){
            sum += get(i);
        }
        int mean = sum/length();
        return mean;
    }
};

int main() {
    
    DynamicArrayWithStats arr = DynamicArrayWithStats();
    arr.append(2);
    arr.append(6);
    arr.append(4);
    arr.append(1);
    arr.append(3);

    cout << "Array: ";
    for(int i = 0; i < arr.length(); i++){
        cout << arr.get(i) << " ";
    }
    cout << endl;
    
    cout << "Max: " << arr.max() << endl;
    cout << "Min: " << arr.min() << endl;
    cout << "Mean: " << arr.mean() << endl;
    return 0;
}