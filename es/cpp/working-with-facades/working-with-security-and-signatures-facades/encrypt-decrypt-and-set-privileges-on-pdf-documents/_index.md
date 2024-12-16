---
title: Encriptar, Desencriptar y establecer privilegios en documentos PDF
type: docs
weight: 10
url: /es/cpp/encrypt-decrypt-and-set-privileges-on-pdf-documents/
---

## <ins>**Establecer privilegios en un archivo PDF existente**
Para establecer privilegios en un documento PDF existente, puedes usar el método **Document->Encrypt(...)**, que toma un objeto **DocumentPrivilege**. La clase **DocumentPrivilege** se utiliza para establecer diferentes privilegios para acceder al documento PDF. Además, hay 4 formas siguientes de usar esta clase:

1. Usando directamente privilegios predefinidos.
1. Basado en un privilegio predefinido y cambiar algunos permisos específicos.
1. Basado en un privilegio predefinido y cambiar alguna combinación específica de permisos de Adobe Professional.
1. Mezcla de las formas 2 y 3.

El siguiente fragmento de código demostrará las 4 formas mencionadas para establecer privilegios en documentos:





{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-SecurityAndSignatures-SetPrivileges-Priveleges.cpp" >}}