#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <bytesobject.h>

/**
 * print_python_bytes - prints python bytes
 *
 * Description: prints python bytes
 *
 * @p: PyObject pointer
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	long int size_of_bytes, i;

	printf("[.] bytes object info\n");
	if (PyBytes_CheckExact(p))
	{
