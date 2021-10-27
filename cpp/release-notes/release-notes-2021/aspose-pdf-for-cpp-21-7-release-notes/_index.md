---
title: Aspose.PDF for C++ 21.7 Release Notes
type: docs
weight: 120
url: /cpp/aspose-pdf-for-cpp-21-7-release-notes/
lastmod: "2021-07-16"
---

{{% alert color="primary" %}}

This page contains release notes information for Aspose.PDF for C++ 21.7.

{{% /alert %}}

## Changes and Improvements

This version of Aspose.PDF for C++ has a codebase of Aspose.PDF for .Net 21.7.

Trailing underscore characters have been removed from the names of header files.
Names of the next public header files have been changed:

| **Old Name** | **Current Name** |
|---|---|
|Aspose.PDF.Cpp/Color__.h|Aspose.PDF.Cpp/Color.h| 
|Aspose.PDF.Cpp/DOM/PageMode_.h|Aspose.PDF.Cpp/DOM/PageMode.h|
|Aspose.PDF.Cpp/Page_.h|Aspose.PDF.Cpp/Page.h|
|Aspose.PDF.Cpp/Rectangle___.h|Aspose.PDF.Cpp/Rectangle.h| 
|Aspose.PDF.Cpp/Text/Font__.h|Aspose.PDF.Cpp/Text/Font.h| 
|Aspose.PDF.Cpp/LoadOptions_.h|Aspose.PDF.Cpp/LoadOptions.h|

## Public API and Backward Incompatible Changes

* Property:Aspose.Pdf.HeaderFooter.IsClipExtraContent
* Type:Aspose.Pdf.OptimizedMemoryStream
* Method:Aspose.Pdf.OptimizedMemoryStream.#ctor
* Method:Aspose.Pdf.OptimizedMemoryStream.#ctor(System.Int32,System.Byte[])
* Method:Aspose.Pdf.OptimizedMemoryStream.#ctor(System.Int32)
* Method:Aspose.Pdf.OptimizedMemoryStream.#ctor(System.Byte[])
* Property:Aspose.Pdf.OptimizedMemoryStream.CanRead
* Property:Aspose.Pdf.OptimizedMemoryStream.CanSeek
* Property:Aspose.Pdf.OptimizedMemoryStream.CanWrite
* Property:Aspose.Pdf.OptimizedMemoryStream.BufferSize
* Property:Aspose.Pdf.OptimizedMemoryStream.Length
* Property:Aspose.Pdf.OptimizedMemoryStream.Position
* Property:Aspose.Pdf.OptimizedMemoryStream.FreeOnDispose
* Method:Aspose.Pdf.OptimizedMemoryStream.Dispose(System.Boolean)
* Method:Aspose.Pdf.OptimizedMemoryStream.Read(System.Byte[],System.Int32,System.Int32)
* Method:Aspose.Pdf.OptimizedMemoryStream.ReadByte
* Method:Aspose.Pdf.OptimizedMemoryStream.Seek(System.Int64,System.IO.SeekOrigin)
* Method:Aspose.Pdf.OptimizedMemoryStream.Flush
* Method:Aspose.Pdf.OptimizedMemoryStream.SetLength(System.Int64)
* Method:Aspose.Pdf.OptimizedMemoryStream.ToArray
* Method:Aspose.Pdf.OptimizedMemoryStream.Write(System.Byte[],System.Int32,System.Int32)
* Method:Aspose.Pdf.OptimizedMemoryStream.WriteByte(System.Byte)
* Method:Aspose.Pdf.OptimizedMemoryStream.WriteTo(System.IO.Stream)
* Field:Aspose.Pdf.OptimizedMemoryStream.DefaultBufferSize
* Property:Aspose.Pdf.XslFoLoadOptions.XsltArgumentList

Complete details of API can be referenced from [Aspose.PDF for C++ API Reference Guide](https://apireference.aspose.com/pdf/cpp).
