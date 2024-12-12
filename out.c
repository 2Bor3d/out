//
// Created by DAVIDGLAENZEL on 12/12/2024.
// https://docs.python.org/3/extending/extending.html
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

int main() {
    printf("\x1B[31m");
    printf("Hello World\n");
    printf("\x1b[31m1\x1b[0m");
    return 0;
  }
