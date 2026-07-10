%global tl_name cfr-initials
%global tl_revision 75712

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.01
Release:	%{tl_revision}.1
Summary:	LaTeX packages for use of initials
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cfr-initials
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cfr-initials.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cfr-initials.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a set of 23 tiny packages designed to make it easier to use
fonts from the initials package in LaTeX, e.g. with the lettrine
package. It is a response to comments on an answer at TeX StackExchange
requesting sample package files for others to copy. I had previously
assumed these were too trivial to be of interest, but if they would be
useful, then I would prefer them to be generally available via CTAN.

