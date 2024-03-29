from spotflow.info import Analysis, MethodPath
from pathspotter.report import html_report, csv_report


def spotflow_after(monitored_program, *args):

    project_name = 'noname'
    report_type = 'both'
    
    if len(args) == 1:
        project_name = args[0]
    if len(args) == 2:
        project_name = args[0]
        report_type = args[1]

    compute_paths(monitored_program)

    if report_type == 'both' or report_type == 'html':
        html_dir = './report_html/' + project_name
        html_report(monitored_program, html_dir)
        print(f"PathSpotter HTML report: {html_dir}")

    if report_type == 'both' or report_type == 'csv':
        csv_dir = './report_csv/' + project_name
        csv_report(monitored_program, csv_dir)
        print(f"PathSpotter CSV report: {csv_dir}")



def compute_paths(monitored_program):

    for monitored_method in monitored_program.all_methods():
        paths = compute_paths_for_method(monitored_method)

        monitored_method.info.paths = paths
        monitored_method.info.total_paths = len(paths)

        monitored_method.info.top1_path_calls = paths[0].call_count
        monitored_method.info.top1_path_ratio = paths[0].call_ratio

        monitored_method.info.top2_path_calls = -1
        monitored_method.info.top2_path_ratio = -1

        monitored_method.info.top3p_path_calls = -1
        monitored_method.info.top3p_path_ratio = -1

        if len(paths) >= 2:
            monitored_method.info.top2_path_calls = paths[1].call_count
            monitored_method.info.top2_path_ratio = paths[1].call_ratio
        
        if len(paths) >= 3:
            sum_call_count_3p = sum(each.call_count for each in paths[2:])
            monitored_method.info.top3p_path_calls = sum_call_count_3p
            monitored_method.info.top3p_path_ratio = round(sum_call_count_3p / monitored_method.info.total_calls, 2)


def compute_paths_for_method(monitored_method):

    most_common_run_lines = Analysis(monitored_method).most_common_run_lines()
    path_pos = 0
    paths = []
    for run_lines in most_common_run_lines:
        path_pos += 1
        distinct_run_lines = run_lines[0]

        equivalent_calls = select_equivalent_calls(monitored_method, distinct_run_lines)
        path = MethodPath(path_pos, distinct_run_lines, equivalent_calls, monitored_method)
        paths.append(path)

    return paths


def select_equivalent_calls(monitored_method, distinct_lines):
    calls = []
    for call in monitored_method.calls:
        if tuple(call.distinct_run_lines()) == tuple(distinct_lines):
            calls.append(call)
    return calls


