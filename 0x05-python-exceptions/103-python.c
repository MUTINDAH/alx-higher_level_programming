#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
    if (!PyList_Check(p)) {
        printf("Error: Invalid PyListObject\n");
        return;
    }

    int size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (int i = 0; i < size; i++) {
        printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
    if (!PyBytes_Check(p)) {
        printf("Error: Invalid PyBytesObject\n");
        return;
    }

    int size = PyBytes_Size(p);
    printf("[*] Python bytes info\n");
    printf("[*] Size of the Python Bytes = %d\n", size);
    printf("[*] First %d bytes: ", size < 10 ? size : 10);
    for (int i = 0; i < (size < 10 ? size : 10); i++) {
        printf("%02x ", PyBytes_AS_STRING(p)[i] & 0xff);
    }
    printf("\n");
}

void print_python_float(PyObject *p)
{
    if (!PyFloat_Check(p)) {
        printf("Error: Invalid PyFloatObject\n");
        return;
    }

    double value = PyFloat_AS_DOUBLE(p);
    printf("[*] Python float info\n");
    printf("[*] Value: %f\n", value);
}

