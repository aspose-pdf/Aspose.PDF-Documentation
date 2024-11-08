---
title: Definir Privilégios em um Arquivo PDF Existente
type: docs
weight: 50
url: /pt/java/set-privileges/
description: Este tópico explica como definir privilégios em um arquivo PDF existente usando a Classe PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Definir Privilégios em um Arquivo PDF Existente (facades)

Para definir os privilégios de um arquivo PDF, crie um objeto da classe [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) e vincule o PDF de entrada usando o método bindPdf. Em seguida, você deve chamar o método setPrivilege para definir os privilégios. Você pode especificar os privilégios usando o objeto [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/DocumentPrivilege) e, em seguida, passar este objeto para o método setPrivilege e salvar o PDF de saída usando o método save.

O trecho de código a seguir mostra como definir os privilégios de um arquivo PDF.

```java
public static void SetPrivilege1() {
        // Criar objeto DocumentPrivileges
        DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
        privilege.setChangeAllowLevel(1);
        privilege.setAllowPrint(true);
        privilege.setAllowCopy(true);

        // Criar objeto PdfFileSecurity
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        fileSecurity.setPrivilege(privilege);
        fileSecurity.save(_dataDir + "sample_privileges.pdf");
    }
```


Veja o seguinte método especificando uma senha:

```java
 public static void SetPrivilege2() {
        // Criar objeto DocumentPrivileges
        DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
        privilege.setChangeAllowLevel(1);
        privilege.setAllowPrint(true);
        privilege.setAllowCopy(true);

        // Criar objeto PdfFileSecurity
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        fileSecurity.setPrivilege("", "P@ssw0rd", privilege);
        fileSecurity.save(_dataDir + "sample_privileges.pdf");
    }
```