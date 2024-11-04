---
title: Criptografar, Descriptografar e definir Privilégios em documentos PDF
type: docs
weight: 10
url: /cpp/encrypt-decrypt-and-set-privileges-on-pdf-documents/
---

## <ins>**Definir Privilégios em um Arquivo PDF Existente**
Para definir privilégios em um documento PDF existente, você pode usar o método **Document->Encrypt(...)**, que leva um objeto **DocumentPrivilege**. A classe **DocumentPrivilege** é usada para definir diferentes privilégios para acessar o documento PDF. Além disso, há 4 maneiras seguintes usando esta classe:

1. Usando privilégio predefinido diretamente.
1. Baseado em um privilégio predefinido e alterar algumas permissões específicas.
1. Baseado em um privilégio predefinido e alterar alguma combinação específica de permissões do Adobe Professional.
1. Mistura do modo 2 e modo 3.

O trecho de código a seguir demonstrará as 4 maneiras acima de definir privilégios de documento:





{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-SecurityAndSignatures-SetPrivileges-Priveleges.cpp" >}}