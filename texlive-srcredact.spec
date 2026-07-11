%global tl_name srcredact
%global tl_revision 38710

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	A tool for redacting sources
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/srcredact
License:	gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/srcredact.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/srcredact.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(srcredact.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a tool to keep a master source, consisting of
different "chunks" intended for different audiences. The tool allows to
extract the versions intended for different audiences and to incorporate
the changes made in any of these versions into the master document. This
work was commissioned by the Consumer Financial Protection Bureau,
United States Treasury.

