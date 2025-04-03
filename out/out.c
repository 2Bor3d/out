#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject* outFunc(PyObject *self, PyObject *args) {
    printf("\x1B[31m");
    printf("Hello World\n");
    printf("\x1b[31m1\x1b[0m");
    return Py_None;
  }

static PyMethodDef outMethodes[] = {
    {"out", outFunc, METH_NOARGS, "Python interface"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef outModule = {
    PyModuleDef_HEAD_INIT,
    "outModule",
//    "Python interface for the fputs C library function",
    NULL,
    -1,
    outMethodes
};

PyMODINIT_FUNC PyInit_out(void) {
    return PyModule_Create(&outModule);
}

