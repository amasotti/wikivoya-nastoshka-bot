from arg_checkers import *  # Funcs to check that the right arguments are specified
from bot.wikidata import get_decimal_coords_from_wd_entity  # WIKIDATA SCRIPTS
from bot.wikivoyage.scripts import *  # WIKIVOYAGE SCRIPTS


# --------------------  RUNNERS -------------------- #

def check_and_run_empty_da_sapere(args):
    """
    Check and run the empty_da_sapere function.

    :param args: The arguments for the function.
    :return: None
    """
    list_empty_daSapere(args.lang)


def check_and_run_sort_template(args):
    """
    :param args: The command line arguments passed to the method.
    :return: None

    This method checks if the necessary template parameters are specified in the command
    line arguments and calls the sort_template_params method accordingly.
    """
    check_template_specified(args)
    sort_template_params(args.target_page, args.target_template, args.lang)


def check_and_run_get_coordinates(args):
    """
    :param args: The command line arguments passed to the method.
    :return: None

    This method checks if the necessary template parameters are specified in the command
    line arguments and calls the sort_template_params method accordingly.
    """
    check_target_entity_specified(args)
    coords = get_decimal_coords_from_wd_entity(args.target_entity, "wikivoyage")
    print(coords)


def check_and_run_fix_empty_dynamicMap(args):
    """
    :param args: The command line arguments passed to the method.
    :return: None

    This method checks if the necessary template parameters are specified in the command
    line arguments and calls the sort_template_params method accordingly.
    """
    check_coords_dynamic_maps(args.lang, args.total)


def check_and_run_categorization_no_destinations(args):
    """
    :param args: The command line arguments passed to the method.
    :return: None

    This method checks if the necessary template parameters are specified in the command
    line arguments and calls the sort_template_params method accordingly.
    """
    check_target_category_specified(args)
    categorize_region_without_destinations(args.target_category)


# --------------------  SCRIPT DISPATCH TABLE -------------------- #

SCRIPT_DISPATCH_TABLE = {
    "empty-da-sapere": check_and_run_empty_da_sapere,
    "sort-template": check_and_run_sort_template,
    "get-coordinates": check_and_run_get_coordinates,
    "fix-empty-dynamicMap": check_and_run_fix_empty_dynamicMap,
    "categorize-region-without-destinations": check_and_run_categorization_no_destinations,
}


def run(args):
    print("Checking for script" + args.script)
    script_function = SCRIPT_DISPATCH_TABLE.get(args.script)

    if script_function is None:
        raise ValueError(f"Unknown script: {args.script}")

    script_function(args)
