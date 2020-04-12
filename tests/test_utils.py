def test_no_trace_logger():
    from zigpy_znp.utils import TraceLogger
    import logging

    assert logging.getLoggerClass() is TraceLogger


def test_existing_trace_logger():
    import logging

    class MyTraceLogger(logging.getLoggerClass()):
        def trace(self):
            pass

    logging.setLoggerClass(MyTraceLogger)

    from zigpy_znp.utils import TraceLogger

    assert logging.getLoggerClass() is not TraceLogger
    assert logging.getLoggerClass() is MyTraceLogger
