import time
import os
import shutil
from DataFileUtil.DataFileUtilClient import DataFileUtil
from KBaseReport.KBaseReportClient import KBaseReport

def log(message, prefix_newline=False):
    """Logging function, provides a hook to suppress or redirect log messages."""
    print(('\n' if prefix_newline else '') + '{0:.2f}'.format(time.time()) + ': ' + str(message))


class Report_creator:
    def __init__(self, config):
        self.config = config
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.dfu = DataFileUtil(self.callback_url)
        self.scratch = os.path.abspath(config['scratch'])

    # -----------------------------------------------------------------
    #    Create a Delimited Table version of the genes in a genome
    #


    def create_report(self, token, ws, report_string, read_file_path):
        # type: (object, object, object, object) -> object
        output_html_files = list()
        output_zip_files = list()
        first_file = ""
        html_string = ""
        html_count = 0
        with open('/kb/module/data/index_start.txt', 'r') as start_file:
            html_string = start_file.read()

        # Make HTML folder
        html_folder = os.path.join(read_file_path, 'html')
        if not os.path.exists(html_folder):
            os.mkdir(html_folder)

        for file in os.listdir(read_file_path):
            label = ".".join(file.split(".")[1:])
            if (file.endswith(".zip")):
                desc = 'Zip file generated by the Report '
                output_zip_files.append({'path': os.path.join(read_file_path, file),
                                         'name': file,
                                         'label': label,
                                         'description': desc})
            elif (file.endswith(".faa")):
                desc = 'FASTA file generated by the Report '
                output_zip_files.append({'path': os.path.join(read_file_path, file),
                                         'name': file,
                                         'label': label,
                                         'description': desc})
            elif (file.endswith(".fna")):
                desc = 'FASTA file generated by the Report '
                output_zip_files.append({'path': os.path.join(read_file_path, file),
                                         'name': file,
                                         'label': label,
                                         'description': desc})
            elif (file.endswith(".txt")):
                desc = 'Text file generated by the Report '
                output_zip_files.append({'path': os.path.join(read_file_path, file),
                                         'name': file,
                                         'label': label,
                                         'description': desc})
            elif (file.endswith(".tab")):
                desc = 'Tab-delimited text file generated by the Report '
                output_zip_files.append({'path': os.path.join(read_file_path, file),
                                         'name': file,
                                         'label': label,
                                         'description': desc})
            elif (file.endswith(".csv")):
                desc = 'Comma-delimited text file generated by the Report '
                output_zip_files.append({'path': os.path.join(read_file_path, file),
                                         'name': file,
                                         'label': label,
                                         'description': desc})
            elif (file.endswith(".gff")):
                desc = 'GFF3 text file generated by the Report '
                output_zip_files.append({'path': os.path.join(read_file_path, file),
                                         'name': file,
                                         'label': label,
                                         'description': desc})
            elif (file.endswith(".html")):
                # Move html into html folder
                shutil.move(os.path.join(read_file_path, file), os.path.join(html_folder, file))

                if (first_file == ""):
                    first_file = file

                html_count += 1

        html_string += "        </div>    </div>    <div id=\"body\">\n"
        html_string += "        <iframe id=\"content\" "
        html_string += "style=\"width: 100%; border: none; \" src=\"" + first_file + "\"></iframe>\n    </div>"

        with open('/kb/module/data/index_end.txt', 'r') as end_file:
            html_string += end_file.read()

        with open(os.path.join(html_folder, "index.html"), 'w') as index_file:
            index_file.write(html_string)

        shock = self.dfu.file_to_shock({'file_path': html_folder,
                                        'make_handle': 0,
                                        'pack': 'zip'})
        desc = 'Open the text Report in a new window'
        output_html_files.append({'shock_id': shock['shock_id'],
                                  'name': 'index.html',
                                  'label': 'HTML Link',
                                  'description': ''})

        report_params = {
            'objects_created': [],
            'message': "Click on Files below to download.\n" + report_string,
            'direct_html': '',
            'direct_html_link_index': None,
            'file_links': output_zip_files,
            'html_links': [],
            'workspace_name': ws,
            'report_object_name': 'Report_util_report'
        }
        if len(report_string) > 1000000:
            report_params = {
                'objects_created': [],
                'message': '',
                'direct_html': 'Links below open text in a new window and click on Files below to download.',
                'direct_html_link_index': None,
                'file_links': output_zip_files,
                'html_links': output_html_files,
                'workspace_name': ws,
                'report_object_name': 'Report_util_report'
            }
        kbase_report_client = KBaseReport(self.callback_url, token=token)
        output = kbase_report_client.create_extended_report(report_params)
        return output
