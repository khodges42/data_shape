import ijson
import pandas as pd
import argparse
import json
import os
#import ijson.backends.yajl2 as ijson

def shape_logs(args, extension, config):
    selected_cols = list(config['columns'])
    trans_cols = filter(lambda x: 'transform' in config['columns'][x], selected_cols)
    with open(args.input, 'r') as f:
        if extension == ".JSON": df = pd.read_json(args.input)
        if extension == ".CSV": df = pd.read_csv(args.input)
        df = df[[x for x in selected_cols if x in list(df)]]
        for tc in [x for x in list(df) if x in trans_cols]:
            df[tc] = df[tc].apply(eval(config['columns'][tc]['transform']))
        return df

def generate_new(args):
    pass

def run(config):
    input_name,input_extension = os.path.splitext(args.input)

    df = shape_logs(args, input_extension.upper(), config)

    if args.generate:
        df = generate(args, df, config)

    if args.output:
        output_name,output_extension = os.path.splitext(args.output)
        if output_extension.upper() == ".CSV":
            df.to_csv(args.output, sep='\t')
        elif output_extension.upper() == ".JSON":
            with open(args.output, 'w') as f:
                f.write(df.to_json())
        else:
            print(df)

if __name__ == '__main__':
    prog = "gen_dataset"
    descr = "Generate or convert datasets"
    parser = argparse.ArgumentParser(prog=prog, description=descr)
    parser.add_argument("--input", type=str, default=None, help="Input Dataset")
    parser.add_argument("--output", type=str, default="./out/", help="Output Dataset")
    parser.add_argument("--config", type=str, default="config.json", help="Config file")
    parser.add_argument("--generate", default=False, help="Generate new data based on the input dataset")
    args = parser.parse_args()
    config = json.load(open(args.config)) if args.config else {"columns": ""}

    run(config)
