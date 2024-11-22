---
title: Generate Crash Reports using C#
linktitle: Create Crash Report
type: docs
weight: 100
url: /net/generate-crash-reports/
description: The main goal of the next code snippets is to handle an exception and generate a crash report that logs the details of the exception using Aspose.PDF for .NET. 
lastmod: "2024-09-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

# Generate a Crash Reports

These code snippets are designed to handle an exception and generate a crash report when an error occurs. 

Here are the detailed steps of the example:

1. The try block contains code that might produce an error. In this case, it deliberately throws a new exception with the message "message" and an inner exception with the message "inner message". The inner exception provides more context about the cause of the error.

1. Catch Block. When an exception is thrown in the try block, the catch block catches it as an Exception object (ex).
Inside the catch block, the PdfException.GenerateCrashReport() method is called. This method is responsible for generating a crash report. The CrashReportOptions object is initialized with the caught exception (ex) and passed to the GenerateCrashReport method as a parameter.

1. Error Handling. It catches exceptions that may occur during the execution of the code.

1. Crash Report Generation. When an error occurs, it automatically creates a crash report that can be used to debug or diagnose the problem later.

**Basic workflow:**

```cs
try
{
    throw new Exception("message", new Exception("inner message"));
}
catch (Exception ex)
{
PdfException.GenerateCrashReport(new CrashReportOptions(ex));
}
```

**Set a directory where crash report will be generated:**

```cs
try
{
    throw new Exception("message", new Exception("inner message"));
}
catch (Exception ex)
{
    CrashReportOptions options = new CrashReportOptions(ex);
    //by default it's working directory of application
    options.CrashReportDirectory = "C:\Temp";

    PdfException.GenerateCrashReport(new CrashReportOptions(ex));
}
```

**Set your own crash report name:**

```cs
try
{
    throw new Exception("message", new Exception("inner message"));
}
catch (Exception ex)
{
    CrashReportOptions options = new CrashReportOptions(ex);

    //by default crash report name will be generated like following:
    //string.Format(@"CrashReport_{0}_{1}.html", DateTime.Today.ToShortDateString(), DateTime.Now.Ticks)
    options.CrashReportFilename = "custom_crash_report_name.html";

    PdfException.GenerateCrashReport(options);
}
```

**Provide additional information about exceptional circumstances in the CustomMessage field:**

```cs
try
{
    throw new Exception("message", new Exception("inner message"));
}
catch (Exception ex)
{
    CrashReportOptions options = new CrashReportOptions(ex);
    options.CustomMessage = "Exception occured while processing PDF files with XFA formated forms";
    PdfException.GenerateCrashReport(options);
}
```

