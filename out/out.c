#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject* outFunc(PyObject *self, PyObject *args) {
    const char *text;
    int color = 29;
    if (!PyArg_ParseTuple(args, "s|i", &text, &color)) {
        return NULL;
    }
    if (color == 29) {
        printf("%s\n", text);
    } else {
        printf("\x1b[%im%s\x1b[0m\n", color, text);
    }

    return Py_None;
  }

static PyMethodDef outMethodes[] = {
    {"out", outFunc, METH_VARARGS, "Python interface"},
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

