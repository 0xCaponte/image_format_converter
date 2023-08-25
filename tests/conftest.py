import pytest
import os
import shutil

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_RESOURCES_DIR = os.path.join(TEST_DIR, 'test_resources')
TEST_RESOURCES_BASELINE_DIR = os.path.join(TEST_DIR, 'test_resources_baseline')

@pytest.fixture(autouse=True)
def prepare_test_resources():

    # Setup: Copy test resources from the baseline 
    print('Preparing test files...')
    if os.path.exists(TEST_RESOURCES_DIR): # Delete old leftover files
        shutil.rmtree(TEST_RESOURCES_DIR)
    
    shutil.copytree(TEST_RESOURCES_BASELINE_DIR, TEST_RESOURCES_DIR) # Copy baseline files

    yield  # wait for test to execute

    # Cleanup
    print('Remove test files...')
    if os.path.exists(TEST_RESOURCES_DIR): 
        shutil.rmtree(TEST_RESOURCES_DIR)
