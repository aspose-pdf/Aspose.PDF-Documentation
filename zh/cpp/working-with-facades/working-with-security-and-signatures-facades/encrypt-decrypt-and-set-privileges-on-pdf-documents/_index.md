---
title: 加密、解密和设置PDF文档的权限
type: docs
weight: 10
url: /zh/cpp/encrypt-decrypt-and-set-privileges-on-pdf-documents/
---

## <ins>**在现有PDF文件上设置权限**
为了在现有PDF文档上设置权限，可以使用**Document->Encrypt(...)**方法，该方法需要一个**DocumentPrivilege**对象。**DocumentPrivilege**类用于设置访问PDF文档的不同权限。此外，使用该类有以下4种方式：

1. 直接使用预定义的权限。
2. 基于预定义的权限并更改一些特定的权限。
3. 基于预定义的权限并更改一些特定的Adobe Professional权限组合。
4. 混合方式2和方式3。

以下代码片段将演示以上4种设置文档权限的方法：