Name:		texlive-srcredact
Version:	38710
Release:	2
Summary:	A tool for redacting sources
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/srcredact
License:	gpl2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/srcredact.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/srcredact.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a tool to keep a master source,
consisting of different "chunks" intended for different
audiences. The tool allows to extract the versions intended for
different audiences and to incorporate the changes made in any
of these versions into the master document. This work was
commissioned by the Consumer Financial Protection Bureau,
United States Treasury.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/scripts/srcredact
%doc %{_texmfdistdir}/texmf-dist/doc/support/srcredact
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/srcredact.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/srcredact.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
