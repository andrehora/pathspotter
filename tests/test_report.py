import unittest
import shutil
import os.path
from spotflow.api import monitor_unittest_testcase
from pathspotter.runner import spotflow_after


class TestReport(unittest.TestCase):

    def test_generate_html_report(self):

        from test.test_email.test_email import TestMessageAPI
        project_name = 'email'
        target_methods = ['email.message._parseparam',
                          'email.message._formatparam',
                          'email.message._splitparam',
                          'email.message._unquotevalue']
        
        monitored_program = monitor_unittest_testcase(TestMessageAPI, target_methods)
        spotflow_after(monitored_program, project_name, 'html')


        self.assertEqual(len(monitored_program), 4)
        self.assertGreaterEqual(len(monitored_program['email.message._parseparam'].calls), 90)
        self.assertGreaterEqual(len(monitored_program['email.message._formatparam'].calls), 30)
        self.assertGreaterEqual(len(monitored_program['email.message._splitparam'].calls), 438)
        self.assertGreaterEqual(len(monitored_program['email.message._unquotevalue'].calls), 90)

        self.assertEqual(len(monitored_program['email.message._parseparam'].info.paths), 3)
        self.assertEqual(len(monitored_program['email.message._formatparam'].info.paths), 4)
        self.assertEqual(len(monitored_program['email.message._splitparam'].info.paths), 2)
        self.assertEqual(len(monitored_program['email.message._unquotevalue'].info.paths), 1)

        path1 = monitored_program['email.message._parseparam'].info.paths[0]
        self.assertEqual(len(path1.path_info.lines), 18)
        self.assertEqual(path1.path_info.run_count, 15)
        self.assertEqual(path1.path_info.not_run_count, 1)
        self.assertEqual(path1.path_info.not_exec_count, 2)
        self.assertGreaterEqual(path1.call_count, 79)
        self.assertEqual(path1.path_info.lines[0].code(), 'def _parseparam(s):')
        self.assertEqual(path1.path_info.lines[0].html(), '<span class="k">def</span> <span class="nf">_parseparam</span><span class="p">(</span><span class="n">s</span><span class="p">):</span>')
        self.assertTrue(path1.path_info.lines[0].is_not_exec())
        self.assertTrue(path1.path_info.lines[1].is_not_exec())
        self.assertTrue(path1.path_info.lines[2].is_run())
        self.assertTrue(path1.path_info.lines[8].is_not_run())

        path2 = monitored_program['email.message._parseparam'].info.paths[1]
        self.assertEqual(len(path2.path_info.lines), 18)
        self.assertEqual(path2.path_info.run_count, 13)
        self.assertEqual(path2.path_info.not_run_count, 3)
        self.assertEqual(path2.path_info.not_exec_count, 2)
        self.assertEqual(path2.call_count, 9)
        self.assertEqual(path2.path_info.lines[0].code(), 'def _parseparam(s):')
        self.assertEqual(path2.path_info.lines[0].html(), '<span class="k">def</span> <span class="nf">_parseparam</span><span class="p">(</span><span class="n">s</span><span class="p">):</span>')
        self.assertTrue(path2.path_info.lines[0].is_not_exec())
        self.assertTrue(path2.path_info.lines[1].is_not_exec())
        self.assertTrue(path2.path_info.lines[2].is_run())
        self.assertTrue(path2.path_info.lines[8].is_not_run())
        self.assertTrue(path2.path_info.lines[13].is_not_run())
        self.assertTrue(path2.path_info.lines[14].is_not_run())

        path3 = monitored_program['email.message._parseparam'].info.paths[2]
        self.assertEqual(len(path3.path_info.lines), 18)
        self.assertEqual(path3.path_info.run_count, 16)
        self.assertEqual(path3.path_info.not_run_count, 0)
        self.assertEqual(path3.path_info.not_exec_count, 2)
        self.assertEqual(path3.call_count, 2)
        self.assertEqual(path3.path_info.lines[0].code(), 'def _parseparam(s):')
        self.assertEqual(path3.path_info.lines[0].html(), '<span class="k">def</span> <span class="nf">_parseparam</span><span class="p">(</span><span class="n">s</span><span class="p">):</span>')
        self.assertTrue(path3.path_info.lines[0].is_not_exec())
        self.assertTrue(path3.path_info.lines[1].is_not_exec())
        self.assertTrue(path3.path_info.lines[2].is_run())

        base_dir = './pathspotter/report_html'
        output_dir = f'{base_dir}/{project_name}'

        self.assert_exists(output_dir)
        self.assert_exists(f'{output_dir}/email.message._parseparam.html')
        self.assert_exists(f'{output_dir}/email.message._formatparam.html')
        self.assert_exists(f'{output_dir}/email.message._splitparam.html')
        self.assert_exists(f'{output_dir}/email.message._unquotevalue.html')
        self.assert_exists(f'{output_dir}/index.html')
        self.assert_exists(f'{output_dir}/style.css')
        self.assert_exists(f'{output_dir}/highlight.css')
        self.assert_exists(f'{output_dir}/coverage_html.js')

        self.delete_dir(base_dir)


    def test_generate_csv_report(self):

        from test.test_email.test_email import TestMessageAPI
        project_name = 'email'
        target_methods = ['email.message._parseparam']

        monitored_program = monitor_unittest_testcase(TestMessageAPI, target_methods)
        spotflow_after(monitored_program, project_name, 'csv')

        self.assertEqual(len(monitored_program), 1)
        self.assertGreaterEqual(len(monitored_program['email.message._parseparam'].calls), 90)

        base_dir = './pathspotter/report_csv'
        output_dir = f'{base_dir}/{project_name}'

        self.assert_exists(output_dir)
        self.assert_exists(f'./{output_dir}/email.message._parseparam.csv')
        self.assert_exists(f'./{output_dir}/index.csv')

        self.delete_dir(base_dir)

    def test_generate_html_csv_report(self):

        from test.test_email.test_email import TestMessageAPI
        project_name = 'email'
        target_methods = ['email.message._parseparam']

        monitored_program = monitor_unittest_testcase(TestMessageAPI, target_methods)
        spotflow_after(monitored_program, project_name)

        base_dir_csv = './pathspotter/report_csv'
        output_dir_csv = f'{base_dir_csv}/{project_name}'
        self.assert_exists(output_dir_csv)

        base_dir_html = './pathspotter/report_html'
        output_dir_html = f'{base_dir_html}/{project_name}'
        self.assert_exists(output_dir_html)

        self.delete_dir(base_dir_csv)
        self.delete_dir(base_dir_html)

    def assert_exists(self, filename):
        self.assertTrue(os.path.exists(filename))

    def delete_dir(self, dir):
        shutil.rmtree(dir)


if __name__ == '__main__':
    unittest.main()
