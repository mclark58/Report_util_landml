# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class Report_util_landml(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def assembly_metadata_report(self, params, context=None):
        """
        The actual function is declared using 'funcdef' to specify the name
        and input/return arguments to the function.  For all typical KBase
        Apps that run in the Narrative, your function should have the 
        'authentication required' modifier.
        :param params: instance of type "AssemblyMetadataReportParams" (A
           'typedef' can also be used to define compound or container
           objects, like lists, maps, and structures.  The standard KBase
           convention is to use structures, as shown here, to define the
           input and output of your function.  Here the input is a reference
           to the Assembly data object, a workspace to save output, and a
           length threshold for filtering. To define lists and maps, use a
           syntax similar to C++ templates to indicate the type contained in
           the list or map.  For example: list <string> list_of_strings;
           mapping <string, int> map_of_ints;) -> structure: parameter
           "assembly_input_ref" of type "assembly_ref", parameter
           "workspace_name" of String, parameter "showContigs" of type
           "boolean" (A boolean. 0 = false, other = true.)
        :returns: instance of type "ReportResults" (Here is the definition of
           the output of the function.  The output can be used by other SDK
           modules which call your code, or the output visualizations in the
           Narrative.  'report_name' and 'report_ref' are special output
           fields- if defined, the Narrative can automatically render your
           Report.) -> structure: parameter "report_name" of String,
           parameter "report_ref" of String
        """
        return self._client.call_method(
            'Report_util_landml.assembly_metadata_report',
            [params], self._service_ver, context)

    def genome_report(self, params, context=None):
        """
        :param params: instance of type "GenomeReportParams" -> structure:
           parameter "genome_input_ref" of type "genome_ref", parameter
           "workspace_name" of String, parameter "report_format" of String
        :returns: instance of type "ReportResults" (Here is the definition of
           the output of the function.  The output can be used by other SDK
           modules which call your code, or the output visualizations in the
           Narrative.  'report_name' and 'report_ref' are special output
           fields- if defined, the Narrative can automatically render your
           Report.) -> structure: parameter "report_name" of String,
           parameter "report_ref" of String
        """
        return self._client.call_method(
            'Report_util_landml.genome_report',
            [params], self._service_ver, context)

    def domain_report(self, params, context=None):
        """
        :param params: instance of type "DomainReportParams" -> structure:
           parameter "domain_annotation_input_ref" of type "domain_ref",
           parameter "evalue_cutoff" of Double, parameter "workspace_name" of
           String, parameter "report_format" of String
        :returns: instance of type "ReportResults" (Here is the definition of
           the output of the function.  The output can be used by other SDK
           modules which call your code, or the output visualizations in the
           Narrative.  'report_name' and 'report_ref' are special output
           fields- if defined, the Narrative can automatically render your
           Report.) -> structure: parameter "report_name" of String,
           parameter "report_ref" of String
        """
        return self._client.call_method(
            'Report_util_landml.domain_report',
            [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('Report_util_landml.status',
                                        [], self._service_ver, context)
