Name:		texlive-cfr-initials
Version:	61719
Release:	2
Summary:	LaTeX packages for use of initials
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cfr-initials
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cfr-initials.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cfr-initials.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a set of 23 tiny packages designed to make it easier to
use fonts from the initials package in LaTeX, e.g. with the
lettrine package. It is a response to comments on an answer at
TeX Stack Exchange (https://tex.stackexchange.com/a/236410/)
requesting sample package files for others to copy. I had
previously assumed these were too trivial to be of interest,
but if they would be useful, then I would prefer them to be
generally available via CTAN.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/cfr-initials
%doc %{_texmfdistdir}/doc/latex/cfr-initials

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
